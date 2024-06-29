package org.galaxio.performance.metrics

import io.gatling.core.Predef._
import org.galaxio.gatling.config.SimulationConfig._
import org.galaxio.performance.metrics.scenarios._

class Debug extends Simulation {

  setUp(
    HttpScenario().inject(atOnceUsers(1)),
  ).protocols(httpProtocol)
    .maxDuration(testDuration)

}
