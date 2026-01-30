
class DispenseEvent:
    """
    Represents a single medication dispensing event for a patient.

    """

    # TODO Task 3: Encode and enforce input constraints (e.g., valid dose, quantity, identifiers)
    def __init__(self, patient_id, medication, dose_mg, quantity):
        """
        Initialize a new DispenseEvent.

        Args:
            patient_id: Unique identifier for the patient receiving medication.
            medication: Name or identifier of the medication being dispensed.
            dose_mg: Dose per unit in milligrams. Must be a positive number.
            quantity: Number of units dispensed. Must be a positive integer.

        """
        if patient_id is None or (isinstance(patient_id, str) and patient_id.strip() == ""):
        raise ValueError("Invalid patient_id")

        if medication is None or (isinstance(medication, str) and medication.strip() == ""):
        raise ValueError("Invalid medication")

        if not isinstance(dose_mg, (int, float)) or dose_mg <= 0:
        raise ValueError("dose_mg must be a positive value")

        if not isinstance(quantity, int) or quantity <= 0:
        raise ValueError("quantity must be a positive integer")
        
        self.patient_id = patient_id
        self.medication = medication

    # TODO Task 4: Define and check system invariants 
    def invariant_holds(existing_events, new_event):
        """
        Check whether adding a new dispense event preserves all system invariants.

        Args:
            existing_events: Iterable of previously recorded DispenseEvent objects.
            new_event: The proposed DispenseEvent to validate.

        Returns:
            bool: True if all invariants hold after adding new_event; False otherwise.
            
        """
        pass
