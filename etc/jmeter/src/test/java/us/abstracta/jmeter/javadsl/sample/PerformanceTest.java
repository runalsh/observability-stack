package us.abstracta.jmeter.javadsl.sample;

import static us.abstracta.jmeter.javadsl.JmeterDsl.*;

import java.io.IOException;
import java.time.Duration;

import org.junit.jupiter.api.Test;

public class PerformanceTest {

  @Test
  public void testPerformance() throws IOException {
    testPlan(
            rpsThreadGroup("MainScenario")
                    .rampToAndHold(1, Duration.ofSeconds(60), Duration.ofSeconds(120))
                    .children(
                            httpSampler("GET /", "http://test.k6.io")
                    ),
            influxDbListener("http://localhost:8428/influx/write")
                    .tag("generator", "perf-1")
                    .percentiles(75.0f, 90.0f, 95.0f, 99.0f, 99.95f, 99.99f)
                    .application("my-app")
                    .measurement("jmeter")
                    .title("capacity"),
            htmlReporter("reports")
    )
            .run();
  }
}