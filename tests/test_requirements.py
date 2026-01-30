import os
import sys
import pytest

# Allow tests to import from /src
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from dispense import DispenseEvent


def test_rejects_invalid_dose_and_quantity():
    # Tests Task 3 constraints: dose must be positive and quantity must be a positive integer
    with pytest.raises(ValueError):
        DispenseEvent("P1", "MedA", 0, 1)

    with pytest.raises(ValueError):
        DispenseEvent("P1", "MedA", -5, 1)

    with pytest.raises(ValueError):
        DispenseEvent("P1", "MedA", 10, 0)

    with pytest.raises(ValueError):
        DispenseEvent("P1", "MedA", 10, 1.5)


def test_duplicate_patient_medication_invariant_fails():
    # Tests Task 4 invariant: same patient cannot receive same medication twice
    class DummyEvent:
        def __init__(self, patient_id, medication, dose_mg):
            self.patient_id = patient_id
            self.medication = medication
            self.dose_mg = dose_mg

    existing_events = [DummyEvent("P1", "MedA", 10)]
    new_event = DummyEvent("P1", "MedA", 20)

    assert DispenseEvent.invariant_holds(existing_events, new_event) is False


def test_invariant_requires_numeric_dose_mg():
    # Tests Task 4 invariant: dose_mg must exist and be numeric
    class DummyEvent:
        def __init__(self, patient_id, medication, dose_mg):
            self.patient_id = patient_id
            self.medication = medication
            self.dose_mg = dose_mg

    invalid_event = DummyEvent("P1", "MedA", "10")
    valid_event = DummyEvent("P1", "MedA", 10)

    assert DispenseEvent.invariant_holds([], invalid_event) is False
    assert DispenseEvent.invariant_holds([], valid_event) is True
# Contains requirement-driven tests for the dispensing subsystem.
# TODO: create at least 3 test cases
