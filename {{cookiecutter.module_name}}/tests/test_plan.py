# -*- coding: utf-8 -*-
import pytest
import tftest


@pytest.fixture
def plan(fixtures_dir):
    tf = tftest.TerraformTest(fixtures_dir)
    tf.setup(extra_files=["plan.auto.tfvars"])
    return tf.plan(output=True)


def test_outputs(plan):
    assert (
        plan.resource_changes["aws_s3_bucket.s3_bucket"]["change"]["after"][
            "tags"
        ]["Environment"]
        == "Dev"
    )
    assert (
        plan.resource_changes["aws_s3_bucket.s3_bucket"]["change"]["after"][
            "tags"
        ]["Name"]
        == "My bucket"
    )


def test_output_attributes(plan):
    assert plan.format_version == "1.0"
    assert plan.terraform_version == "1.1.8"
