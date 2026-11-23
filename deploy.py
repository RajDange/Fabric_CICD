import argparse, os
from azure.identity import ClientSecretCredential
from fabric_cicd import FabricWorkspace, publish_all_items

p = argparse.ArgumentParser()
p.add_argument("--workspace_id", required=True)
p.add_argument("--environment", required=True)
a = p.parse_args()

cred = ClientSecretCredential(
    os.environ["AZURE_TENANT_ID"],
    os.environ["AZURE_CLIENT_ID"],
    os.environ["AZURE_CLIENT_SECRET"],
)

ws = FabricWorkspace(
    workspace_id=a.workspace_id,
    environment=a.environment,
    repository_directory="./Fabric_POC",   # must match the folder you connected in Fabric
    item_type_in_scope=["Notebook"],
    token_credential=cred,
)
publish_all_items(ws)