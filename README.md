# Friends and Assistant Candidates Management

This repository contains Python scripts for managing friends and determining eligibility to be an assistant based on academic performance.

## File: `Listas_1.py`
### `serAsistente` Function:
  Displays questions to determine if the user is eligible to be an assistant based on academic performance.

## File: `funciones_1.py`
### `ingresarMaterias` Function:
  Allows the user to input subjects, converting them to uppercase.

### `ingresarNotas` Function:
- **Description:**
  Allows the user to input grades for subjects.

### `indicarPromedio` Function:
- **Description:**
  Calculates the average of the grades list.

### `saberResultado` Function:
- **Description:**
  Indicates whether the user can be an assistant based on the provided information.

## File: `Listas_2.py`
### Program:
- Calls `ingresarAmigos()` and prints the birthday calendar.
- Calls `saberSexo(amigos)` to determine the number of male and female friends.

### Variables:
- `amigos`: List containing friend details.
- `meses`: List containing months and friend counts.
- `aux`: List containing possible values for gender (1 for male, 2 for female).
- `hombres`: List to store male friends.
- `mujeres`: List to store female friends.

## File: `funciones_2.py`
### `ingresarAmigos` Function:
  Allows the user to input friends, their birth months, and genders.

### `diaAux` Function:
  Validates the entered day.


### `SaberSexoAux` Function:
  Validates the entered gender.

### `contarMeses` Function:
  Counts the number of friends in each month and validates month entries.

### `imprimirResultado` Function:
  Prints the list of friends and their birthdays.

### `saberSexo` Function:
  Calculates the number of male and female friends.
