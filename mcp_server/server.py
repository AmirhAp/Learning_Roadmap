import json
from pathlib import Path

from mcp.server import MCPServer
from mcp.types import ToolAnnotations
from mcp_server.schema import Lesson, LessonResult, RoadmapList, RoadmapSummary


DATA_FILE = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "roadmaps.json"
)


def load_catalog() -> dict:
    with DATA_FILE.open(encoding="utf-8") as file:
        return json.load(file)


mcp = MCPServer(
    "learning-roadmap-tools",
    instructions=(
        "Read-only learning roadmap tools. "
        "Use get_lesson to retrieve existing lesson outlines. "
        "Do not claim that these tools read or update Notion."
    ),
)


@mcp.tool(
    annotations=ToolAnnotations(
        read_only_hint=True,
        open_world_hint=False,
    )
)
def list_roadmaps() -> RoadmapList:
    """List available roadmaps from the local catalog."""
    catalog = load_catalog()

    return RoadmapList(
        roadmaps=[
            RoadmapSummary(
                id=roadmap_id,
                title=record["title"],
            )
            for roadmap_id, record in catalog.items()
        ]
    )


@mcp.tool(
    annotations=ToolAnnotations(
        read_only_hint=True,
        open_world_hint=False,
    )
)
def get_lesson(roadmap_id: str, session_id: str) -> LessonResult:
    """Fetch a lesson by exact roadmap and session IDs."""
    catalog = load_catalog()

    roadmap = catalog.get(roadmap_id)

    if roadmap is None:
        return LessonResult(
            ok=False,
            roadmap_id=roadmap_id,
            session_id=session_id,
            error="ROADMAP_NOT_FOUND",
        )

    lesson_data = roadmap["sessions"].get(session_id)

    if lesson_data is None:
        return LessonResult(
            ok=False,
            roadmap_id=roadmap_id,
            session_id=session_id,
            error="LESSON_NOT_FOUND",
        )

    return LessonResult(
        ok=True,
        roadmap_id=roadmap_id,
        session_id=session_id,
        lesson=Lesson(**lesson_data),
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
