# -*- coding: utf-8 -*-
import pytest
import tftest


@pytest.fixture
def output(fixtures_dir):
    tf = tftest.TerraformTest(fixtures_dir)
    tf.setup()
    tf.apply(**{"auto_approve": True})
    yield tf.output()
    tf.destroy(**{"auto_approve": True})


def test_apply(output):
    assert output["arn"] == "arn:aws:s3:::test"
    assert output["name"] == "test"
