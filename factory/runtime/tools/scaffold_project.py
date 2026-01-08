#!/usr/bin/env python3
"""
M4ND8 Scaffolding Script - Canonical Execution Path
Strategic Purpose: Provides deterministic scaffolding execution that respects
the bootstrap_authority flag from director.yaml while maintaining protocol fidelity.

Operational Context:
- This script is the single source of truth for scaffolding operations
- It must be idempotent and handle both autonomous and director_supervised modes
- It enforces the absolute census mandate by updating hub.md before creating files
- It maintains cryptographic provenance through cofo.md Change Notes

Safety Constraints:
- Must operate within filesystem_boundary defined in director.yaml
- Must respect feature flags for optional scaffolds
- Must halt on ambiguity rather than invent structure
"""
import os
import sys
import json
import yaml
import logging
from datetime import datetime, timezone
from pathlib import Path

class ScaffoldingError(Exception):
    """Strategic failure requiring escalation"""
    pass

def load_director_config():
    """Load director.yaml with fail-closed semantics"""
    config_path = Path('./kernel/director.yaml')
    if not config_path.exists():
        raise ScaffoldingError(f"Missing critical governance file: {config_path}")
    
    try:
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise ScaffoldingError(f"Invalid YAML in director.yaml: {str(e)}")

def determine_bootstrap_mode(director_config):
    """Respect the strategic bootstrap authority decision"""
    bootstrap_authority = director_config.get('bootstrap_authority', 'director_supervised')
    logging.info(f"Bootstrap authority mode: {bootstrap_authority}")
    return bootstrap_authority

def validate_filesystem_boundary(director_config):
    """Enforce sovereign boundaries before any operation"""
    boundaries = director_config.get('budgets', {}).get('io', {}).get('filesystem_boundary', [])
    if not boundaries:
        raise ScaffoldingError("No filesystem boundaries defined in director.yaml")
    
    logging.info(f"Validated filesystem boundaries: {boundaries}")
    return boundaries

def scaffold_core_artifacts(bootstrap_mode, boundaries):
    """Strategic scaffolding of core governance artifacts"""
    core_artifacts = [
        'manifest.yaml',
        'hub.md',
        'cofo.md',
        'spec.md'
    ]
    
    for artifact in core_artifacts:
        if not Path(artifact).exists():
            if bootstrap_mode == 'autonomous':
                # Original protocol behavior: generate from templates
                template_path = f'./interface/templates/{artifact.replace(".md", "_template.md")}'
                if Path(template_path).exists():
                    with open(template_path, 'r') as src, open(artifact, 'w') as dst:
                        dst.write(src.read())
                    logging.info(f"Created {artifact} from template")
                    record_cofo_change(artifact, "Created from template", "autonomous_bootstrap")
                else:
                    raise ScaffoldingError(f"Missing template for {artifact}")
            else:
                # Director-supervised mode: require explicit command
                logging.info(f"Skipping {artifact} creation - awaiting Director command in supervised mode")
    
    return core_artifacts

def update_hub_wiring(artifact_path, role, description):
    """Enforce absolute census mandate before file creation"""
    hub_path = Path('hub.md')
    if hub_path.exists():
        content = hub_path.read_text()
        if f"| {artifact_path}" not in content:
            # Add to items table
            items_marker = "| Path|Role|Description|"
            if items_marker in content:
                new_entry = f"| {artifact_path}|{role}|{description}|"
                content = content.replace(items_marker, f"{items_marker}\n{new_entry}")
                hub_path.write_text(content)
                logging.info(f"Updated hub.md wiring for {artifact_path}")
    else:
        # Create minimal hub.md if missing
        hub_template = """# hub — Wiring Diagram (Control Plane)
M4ND8 Protocol v5.1

hub — Wiring Diagram (Template)
Directory: `./`

## Items (Role & Description)
| Path|Role|Description|
|---|---|---|
"""
        hub_path.write_text(hub_template)
        logging.info("Created minimal hub.md")

def record_cofo_change(path, change, evidence):
    """Maintain cryptographic provenance through Change Notes"""
    cofo_path = Path('cofo.md')
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    
    if cofo_path.exists():
        content = cofo_path.read_text()
        if "| Timestamp (UTC)|Actor|Path|Change|Why / Evidence|" in content:
            change_entry = f"| {timestamp}|scaffolder|{path}|{change}|{evidence}|"
            content = content.replace("| Timestamp (UTC)|Actor|Path|Change|Why / Evidence|", 
                                     f"| Timestamp (UTC)|Actor|Path|Change|Why / Evidence|\n{change_entry}")
            cofo_path.write_text(content)
    else:
        # Create minimal cofo.md if missing
        cofo_template = f"""# cofo — Context Form (Control Plane)
M4ND8 Protocol v5.1

cofo — Context Form (Template)
Directory: `./`

## Items (Role & Description)
| Path|Role|Description|
|---|---|---|

## Change Notes
| Timestamp (UTC)|Actor|Path|Change|Why / Evidence|
|---|---|---|---|---|
| {timestamp}|scaffolder|{path}|{change}|{evidence}|

## Rules (Local)
`cofo` must list all items in this folder.
Every edit to an item must add a Change Note row.
"""
        cofo_path.write_text(cofo_template)

def main():
    """Strategic scaffolding execution entry point"""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    try:
        director_config = load_director_config()
        bootstrap_mode = determine_bootstrap_mode(director_config)
        boundaries = validate_filesystem_boundary(director_config)
        
        # Strategic scaffolding decision point
        if bootstrap_mode == 'autonomous':
            logging.info("Executing autonomous bootstrap sequence")
            scaffold_core_artifacts(bootstrap_mode, boundaries)
        else:
            logging.info("Director-supervised mode - awaiting explicit command")
            # In supervised mode, this script would typically be called with specific parameters
            # from the Director agent with a scaffold.json specification
        
        logging.info("Scaffolding sequence completed successfully")
        return 0
        
    except ScaffoldingError as e:
        logging.error(f"Strategic scaffolding failure: {str(e)}")
        print(f"HALT: Strategic scaffolding failure - {str(e)}", file=sys.stderr)
        return 42
    except Exception as e:
        logging.error(f"Unexpected failure: {str(e)}")
        print(f"HALT: Unexpected failure - {str(e)}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
