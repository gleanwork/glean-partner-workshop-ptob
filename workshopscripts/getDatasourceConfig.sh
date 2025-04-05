curl -X POST \
  https://support-lab-be.glean.com/api/index/v1/getdatasourceconfig \
  -H 'Authorization: Bearer <INSERT_GLEAN_INDEXING_API_TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "datasource": "ptobpartnerwsXX"
  }'