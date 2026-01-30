<How should the system identify a patient, and are there any rules about what makes a patient identifier valid or invalid?, Constraint>
This is a constraint because it limits what kind of values are allowed to be used as a patient identifier, and the system cannot accept identifiers that do not meet those rules.

<How should medications be identified in the system, and will the system work with free text names or only with a predefined list of medications?, Constraint>
This is a constraint because it restricts how medications can be entered into the system, and it defines boundaries on what the system is allowed to accept as a medication.

<What information must be provided when a medication is dispensed, and are there any fields that are optional or can be left empty?, Functional Requirement>
This is a functional requirement because it describes what the system is expected to do, which is to collect and store specific pieces of information whenever a medication is dispensed.

<How should the system decide whether a dose value is acceptable, and what should happen if the dose is zero, negative, or not given in milligrams?, Constraint>
This is a constraint because it places clear limits on what dose values are allowed, and it explains that certain values should be rejected before the system accepts the dispensing event.

<How should the system determine the maximum allowed daily dose for a medication, and where should this information come from?, Functional Requirement>
This is a functional requirement because the system must be able to check or look up information about maximum daily doses in order to decide whether a dispensing event is valid.

<How should the system behave if a user attempts to dispense more medication than the maximum daily dose allows?, Constraint>
This is a constraint because it defines a hard limit that the system must not allow to be crossed, and the system must stop the action if the rule is broken.

<How does the system define the same day when checking whether a patient has already received a specific medication, and how should this be tracked?, Invariant>
This is an invariant because it describes a rule that must always stay true over time, meaning that the system must consistently make sure the same patient does not receive the same medication more than once in a day.

<What should the system do if a patient is dispensed the same medication more than once in a single day, and should this be blocked or only flagged as a warning?, Invariant>
This is an invariant because it is still about protecting a rule that must always hold in the system, and the system needs to respond in a way that keeps that rule from being broken.
