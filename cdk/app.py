#!/usr/bin/env python3

import os

from aws_cdk import core as cdk

# For consistency with TypeScript code, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

from cdk.cdk_stack import CdkStack

aws_region = os.environ.get("AWS_DEFAULT_REGION", "us-east-1")
aws_account = os.environ.get("AWS_ACCOUNT_ID", "")


app = cdk.App()
CdkStack(
    app,
    "valheim-server-stack",
    env={"region": aws_region, "account": aws_account}
)

app.synth()
