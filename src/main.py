import json
from typing import Dict, Any

import typer
from pydantic import BaseModel
from retro_funding_metrics import get_s7_devtooling_metrics

app = typer.Typer()

class MetricsResult(BaseModel):
    """Base model for metrics results"""
    success: bool
    data: Dict[str, Any]
    message: str = ""

@app.command()
def fetch_metrics(
    output_file: str = typer.Option(None, help="Output file path (optional)"),
) -> None:
    """
    Run the retro funding metrics script and return results as JSON.
    Can be called from GitHub Actions or command line.
    """
    try:
        # Get the metrics data
        metrics_data = get_s7_devtooling_metrics()
        
        result = MetricsResult(
            success=True,
            data={"metrics": metrics_data},
            message="Retro funding metrics retrieved successfully"
        )
        
        # Convert to JSON
        output_json = result.model_dump_json(indent=2)
        
        # Write to file if specified
        if output_file:
            with open(output_file, 'w') as f:
                f.write(output_json)
        
        # Print row count instead of full output
        row_count = len(metrics_data)
        print(f"Successfully processed {row_count} metrics rows")
        
    except Exception as e:
        error_result = MetricsResult(
            success=False,
            data={},
            message=str(e)
        )
        print(error_result.model_dump_json(indent=2))
        raise typer.Exit(1)

if __name__ == "__main__":
    app() 