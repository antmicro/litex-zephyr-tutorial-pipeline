# LiteX Zephyr tutorial pipeline

This is a testing pipeline for [the Zephyr tutorial hosted on the LiteX-BuildEnv wiki](https://github.com/timvideos/litex-buildenv/wiki/Zephyr).

The script extracts relevant code snippets and executes the whole workflow: clones the LiteX-BuildEnv repository, builds the relevant software within the [Conda environment](https://anaconda.org/anaconda/conda) and runs it in [Renode](https://renode.io).

The test is executed by [Travis CI](https://travis-ci.com/antmicro/litex-zephyr-tutorial-pipeline).
