# Blender Lab MCP and Codex

Instructor-requested addition for 19 November 2026. Reuses the course's existing
Blender scene, Python API explanation, visual comparisons and Godot GLB handoff.

Primary source: [Blender Lab MCP](https://www.blender.org/lab/mcp-server/) and
its [source repository](https://projects.blender.org/lab/blender_mcp).
Checked source revision and observed upstream HEAD:
`dbbf836ad4b1025f14a2b3b504c43903f39e0b04`.

- `readme.md`: Blender add-on plus separate MCP process, stdio/TCP boundaries.
- `mcp/README.md`: install the add-on from `https://lab.blender.org/`.
- `mcp/pyproject.toml`: `blender-mcp` 1.0.2, Python >=3.10.
- `addon/blender_mcp_addon/blender_manifest.toml`: MCP add-on 1.0.0,
  Blender >=5.1, GPL-3.0-or-later.
- `addon/blender_mcp_addon/__init__.py`: online-access prerequisite,
  host/port preferences, start/stop controls and running status.
- `mcp/blmcp/tools_helpers/connection.py`: BLENDER_MCP_HOST/PORT and port 9876.
- `mcp/blmcp/tools/execute_blender_code.py`: `code` argument, `result` return
  dictionary and embedded bpy execution. Dedicated inspection tools are preferred
  when they cover the requested operation.

Client reference: [Codex MCP](https://developers.openai.com/codex/extend/mcp).
Current command/configuration syntax was retrieved through Context7 for
`/openai/codex` and checked against the installed `codex mcp add --help`.
The PFAD README provides the pinned uvx invocation and equivalent TOML.

The configured Codex tools returned live scene state and a Blender window image
on 19 November. The scene was being driven by another session and was not edited,
saved, reset or closed during those read-only checks. Existing Sculpture renders
remain the separately labelled 18 November author rehearsal, not a captured MCP
agent episode. The Lab server is distinct from Ahuja's community bridge retained
in the optional PFAD appendix. No third-party source code is copied into this deck.
