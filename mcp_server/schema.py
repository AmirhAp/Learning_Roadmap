from pydantic import BaseModel


class RoadmapSummary(BaseModel):
    id: str
    title: str


class RoadmapList(BaseModel):
    roadmaps: list[RoadmapSummary]


class Lesson(BaseModel):
    title: str
    objectives: list[str]
    topics: list[str]
    prerequisites: list[str]


class LessonResult(BaseModel):
    ok: bool
    roadmap_id: str
    session_id: str
    lesson: Lesson | None = None
    error: str | None = None