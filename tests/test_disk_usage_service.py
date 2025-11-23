import pytest
from netly_services.DiskUsageService import DiskUsageService
from unittest.mock import patch


def test_check_name():
    assert DiskUsageService.get_service_name() == "disk_usage"


@pytest.mark.parametrize(
    "parameters, expected_mount_point",
    [
        ({"mount_point": "/mnt"}, "/mnt"),  # podany mount_point
        (None, "/"),  # brak parametrów → użycie domyślnego "/"
        ({}, "/"),  # pusty słownik → też "/"
    ],
)
def test_disk_usage_success(parameters, expected_mount_point):
    # mock wartości dysku
    mock_disk = (100 * 2**30, 50 * 2**30, 50 * 2**30)

    with patch("shutil.disk_usage", return_value=mock_disk) as mock_func:
        result = DiskUsageService.get_data(parameters=parameters)

        # sprawdzamy, że funkcja wywołała shutil.disk_usage z oczekiwanym mount_point
        mock_func.assert_called_once_with(expected_mount_point)

        # sprawdzamy wynik
        assert result.status == "Success"
        assert result.metadata["total"] == 100
        assert result.metadata["used"] == 50
        assert result.metadata["free"] == 50
        assert result.metadata["unit"] == "GB"


@pytest.mark.parametrize(
    "parameters, expected_mount_point",
    [
        ({"mount_point": "/mnt"}, "/mnt"),
        (None, "/"),
        ({}, "/"),
    ],
)
def test_disk_usage_file_not_found(parameters, expected_mount_point):
    with patch(
        "shutil.disk_usage", side_effect=FileNotFoundError("No such mount")
    ) as mock_func:
        result = DiskUsageService.get_data(parameters=parameters)
        mock_func.assert_called_once_with(expected_mount_point)
        assert result.status == "Failed"
        assert "No such mount" in result.output
        assert result.metadata == {}
