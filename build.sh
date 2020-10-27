#!/usr/bin/env bash
yarn install -d  @openapitools/openapi-generator-cli
npx @openapitools/openapi-generator-cli generate -i https://raw.githubusercontent.com/opsgenie/opsgenie-oas/master/swagger.yaml -g python -o ./ --skip-validate-spec

