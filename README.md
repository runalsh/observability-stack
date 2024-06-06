### Observability stack 

from https://github.com/runalsh/easylinux

All services under reverse proxy (caddy, angie). Access to services available via overlay network (tailscale and zerotier).

LAB path: kafka lab (producer py + consumer py + 3 kafka nodes (zookeeper) + jwt)

Contain:

      Metrics aggregation: prometheus, victoriametrics
      Metrics scrape: vmagent (victoriametrics), pushgateway
      Logs aggregation: loki, victorialogs
      Exporters: node_exporter, cadvizor, blackbox-exporter, promtail
      Aletring: alertmanager, vmalert
      UI: grafana
      Storage: minio
      SEC: keycloak
      
      Other: watchtower, tailscale, zerotier, certbot, angie, caddy, postgres

TODO:

    Save (or backup) metrics and logs to minio-s3
    Thanos as HA storage
    Clickhouse \ OpenSearch as logs storage
    Sentry
    Open Telemetry collector
    Vector
    Tetragon (ebpf)
    Open tracing 
    Jaeger
    Try to make apps on py and go with tracing
