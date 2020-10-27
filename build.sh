#!/usr/bin/env bash
yarn install -d  @openapitools/openapi-generator-cli
npx @openapitools/openapi-generator-cli generate -i ./swagger.json -g python -o ./ --skip-validate-spec

