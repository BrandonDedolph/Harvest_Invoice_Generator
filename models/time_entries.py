from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    name: str

class Client(BaseModel):
    id: int
    name: str
    currency: str

class Project(BaseModel):
    id: int
    name: str
    code: str

class Task(BaseModel):
    id: int
    name: str

class UserAssignment(BaseModel):
    id: int
    is_project_manager: bool
    is_active: bool
    use_default_rates: bool
    budget: Optional[float]
    created_at: datetime
    updated_at: datetime
    hourly_rate: Optional[float]

class TaskAssignment(BaseModel):
    id: int
    billable: bool
    is_active: bool
    created_at: datetime
    updated_at: datetime
    hourly_rate: Optional[float]
    budget: Optional[float]

class TimeEntry(BaseModel):
    id: int
    spent_date: str
    hours: float = Field(ge=0)  # hours must be non-negative
    hours_without_timer: float = Field(ge=0)
    rounded_hours: float = Field(ge=0)
    notes: Optional[str]
    is_locked: bool
    locked_reason: Optional[str]
    is_closed: bool
    is_billed: bool
    timer_started_at: Optional[datetime]
    started_time: Optional[str]
    ended_time: Optional[str]
    is_running: bool
    billable: bool
    budgeted: bool
    billable_rate: Optional[float]
    cost_rate: Optional[float]
    created_at: datetime
    updated_at: datetime
    user: User
    client: Client
    project: Project
    task: Task
    user_assignment: UserAssignment
    task_assignment: TaskAssignment
    invoice: Optional[dict]
    external_reference: Optional[str]

class TimeEntries(BaseModel):
    entries: List[TimeEntry]
