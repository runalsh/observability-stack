### Observability stack 

All services under a reverse proxy (like nginx, Caddy) with basic auth and HTTPS. 

Access to services available via overlay networks (Tailscale and ZeroTier).

Contain:

      Metrics aggregation: prometheus, victoriametrics, vector
      Metrics scrape: vmagent (victoriametrics), pushgateway, telegraf
      Logs aggregation: loki, victorialogs, cloki
      Exporters: node_exporter, cadvizor, blackbox-exporter, promtail
      Aletring: alertmanager, vmalert
      UI: grafana
      Storage: minio (save metrics and logs), influxdb, thanos, clickhouse
      SEC: keycloak
      Log generation: flog, log-generator (apache, from pip), opentelemetry, gatling, jmeter
      Traces: jaeger
      Other: watchtower, tailscale, zerotier, certbot, angie, caddy, postgres, 
            portainer + docker socket proxy, qryn

      Full stacks: 
            ./elasticsearch - ELK/EFK and ELK+ (ELK+Filebeat+Kafka)
            Logs from generators are read by Filebeat and sent to Kafka. Logstash
            reads logs from the topic and pushes them to Elasticsearch.
            ./opensearch - OLOD (Opensearch, Logstash, Opensearch-Dashboard)
            
      LABS:
          ./LABS/kafka - Kafka lab (producer + consumer+ 3 Kafka + JWT + Prometheus + Grafana)
        producer2.py writes JSON messages to Kafka and Kafka Connect writes them to Postgres. 
        You can see messages from Kafka in Kafdrop or using consumer.py.
          ./LABS/kafka-wo-zoo - Kafka lab without Zookeeper, using Bitnami images

TODO:

    Sentry
    
    Tetragon (ebpf)
    YDB instead Kafka (what?! yes! :) )
    OpenTracing 
