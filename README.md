### Observability stack 

All services under reverse proxy (angie, caddy) with basic auth and https. Access to services available via overlay network (tailscale and zerotier).

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
      
      Log generation: flog, log-generator (apache, from pip)

      Other: watchtower, tailscale, zerotier, certbot, angie, caddy, postgres, docker socket proxy

TODO:

    done Save (or backup) metrics and logs to minio-s3
    Thanos as HA storage
    Clickhouse \ OpenSearch as logs storage
    Sentry
    OpenTelemetry collector
    Vector
    Tetragon (ebpf)
    OpenTracing 
    Jaeger
    Try to make apps on py and go with tracing or add auto-tracing tool
