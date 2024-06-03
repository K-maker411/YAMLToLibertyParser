from pathlib import Path
import pytest
from src.attributes_provider import AttributesProvider

SIMPLE_ATTRIBUTES_LIST = {
  "bus_naming_style": {"type": ["string"]},
  "comment": {"type": ["string"]},
  "current_unit": {"type": ["valueenum"]},
  "date": {"type": ["date"]},
  "delay_model": {"type": ["valueenum"]},
  "em_temp_degradation_factor": {"type": ["float"]},
  "fpga_technology": {"type": ["fpga_technology_name_string"]},
  "in_place_swap_mode": {"type": ["valueenum"]},
  "input_threshold_pct_fall": {"type": ["trip_point_value"]},
  "input_threshold_pct_rise": {"type": ["trip_point_value"]},
  "leakage_power_unit": {"type": ["valueenum"]},
  "nom_calc_mode": {"type": ["nameid"]},
  "nom_process": {"type": ["float"]},
  "nom_temperature": {"type": ["float"]},
  "nom_voltage": {"type": ["float"]},
  "output_threshold_pct_fall": {"type": ["trip_point_value"]},
  "output_threshold_pct_rise": {"type": ["trip_point_value"]},
  "piece_type": {"type": ["valueenum"]},
  "power_model": {"type": ["table_lookup", "polynomial"]},
  "preferred_output_pad_slew_rate_control": {"type": ["valueenum"]},
  "preferred_input_pad_voltage": {"type": ["string"]},
  "preferred_output_pad_voltage": {"type": ["string"]},
  "pulling_resistance_unit": ["1ohm", "10ohm", "100ohm", "1kohm"],
  "revision": {"type": ["float", "string"]},
  "simulation": [True, False],
  "slew_derate_from_library": {"type": ["derate_value"]},
  "slew_lower_threshold_pct_fall": {"type": ["trip_point_value"]},
  "slew_lower_threshold_pct_rise": {"type": ["trip_point_value"]},
  "slew_upper_threshold_pct_fall": {"type": ["trip_point_value"]},
  "slew_upper_threshold_pct_rise": {"type": ["trip_point_value"]},
  "time_unit": ["1ps", "10ps", "100ps", "1ns"],
  "voltage_unit": ["1mV", "10mV", "100mV", "1V"]
}



def test_get_library_level_simple_attributes(attributes_provider):
  assert attributes_provider.get_library_level_simple_attributes(
  ) == SIMPLE_ATTRIBUTES_LIST

# TODO - add tests for get_library_level_default_attributes and get_library_level_scaling_attributes