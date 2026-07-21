from sqlalchemy.orm import Session
import models, schemas


def get_employees(db: Session):
    """Retrieve all employees from the database."""
    return db.query(models.Employee).all()


def get_employee(db: Session, emp_id: int):
    """
    Retrieve a single employee by their ID.
    Returns None if no employee with the given ID exists.
    """
    return (
        db
        .query(models.Employee)
        .filter(models.Employee.id == emp_id)  # Filter by primary key
        .first()                                # Return first match or None
    )


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    """
    Create and persist a new employee record.
    Commits the transaction and refreshes the instance to reflect DB-generated values (e.g., ID).
    """
    # Instantiate a new Employee model from the incoming schema data
    db_employee = models.Employee(
        name=employee.name,
        email=employee.email
    )

    db.add(db_employee)      # Stage the new record for insertion
    db.commit()              # Persist the transaction to the database
    db.refresh(db_employee)  # Sync the instance with DB state (e.g., auto-generated ID)
    return db_employee


def update_employee(db: Session, emp_id: int, employee: schemas.EmployeeUpdate):
    """
    Update an existing employee's details by ID.
    Returns the updated employee, or None if no matching record is found.
    """
    # Fetch the existing employee record
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()

    if db_employee:
        # Apply the updated field values from the schema
        db_employee.name = employee.name
        db_employee.email = employee.email

        db.commit()              # Persist the changes
        db.refresh(db_employee)  # Sync to reflect any DB-side updates

    return db_employee  # Returns None if employee was not found


def delete_employee(db: Session, emp_id: int):
    """
    Delete an employee record by ID.
    Returns the deleted employee object, or None if no match was found.
    """
    # Look up the employee before attempting deletion
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()

    if db_employee:
        db.delete(db_employee)  # Mark the record for deletion
        db.commit()             # Commit the deletion to the database

    return db_employee  # Returns the deleted object (or None if not found)