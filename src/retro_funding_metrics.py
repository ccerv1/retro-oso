from dotenv import load_dotenv
import json
import os
import pandas as pd
from pyoso import Client

def get_s7_devtooling_metrics():
    load_dotenv()
    oso_client = Client(os.getenv("OSO_API_KEY"))
    df_metrics = oso_client.to_pandas("""
        SELECT
            p.project_id AS oso_project_id,
            p.project_name AS op_atlas_project_id,
            p.display_name AS project_name,
            pbc.collection_name AS round_id,
            metrics.is_eligible,
            metrics.package_connection_count,
            metrics.developer_connection_count,
            metrics.onchain_builder_oso_project_ids,
            metrics.onchain_builder_op_atlas_ids,
            metrics.trusted_developer_usernames
        FROM int_superchain_s7_devtooling_metrics_by_project AS metrics
        JOIN projects_by_collection_v1 AS pbc
            ON metrics.project_id = pbc.project_id
        JOIN projects_v1 AS p
            ON pbc.project_id = p.project_id
        WHERE collection_name = '7-2'
    """)
    
    return json.loads(df_metrics.to_json(orient='records')) 
