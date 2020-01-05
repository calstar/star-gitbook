# Testing

Testing is an important component of aerospace development. By abiding by team-wide testing guidelines, tests provide useful insight to the state of hardware and software in the rocket.

## Testing Terminology

* HIL testing - Hardware In-loop Testing
* SIL testing - Software In-loop Testing \(no hardware\)

## Test Procedure Development Guidelines

### The Most Important Things

Written test procedures should follow two primary directives:

1. **Reproducibility and clarity of instruction**: A written test procedure should be detailed enough that someone on the subteam should be able to follow it without having been directly involved in creating the test procedure
2. **Expectation of result**: A written test procedure should outline the expected result of the test and how to document the results or any anomalies.

### Also Important

_Tests need to be performed and recorded in order for them to have value_. Tests done in support of internal design reviews MUST be recorded to be considered valid. Testing needs to be recorded during major design or development milestones so that we have a history of the development.

For testing to have a positive impact on the reliability of our launch vehicles, launches should not occur unless tests are passed by all components of the rocket, both in component form as well as during post-integration.

## **Subteam-Specific Guidelines**

### Avionics

1. Any software-related \(HIL or SIL\) testing should have test software associated with each related test, to facilitate reproducibility of that test.
2. Hardware testing should begin with basic board debugging techniques, as described in the Avionics Gitbook page [Debugging Tips](https://calstar.gitbook.io/docs/tutorials/electrical-and-software/debugging-tips). This is to ensure there are no defects or obvious design bugs before software-hardware integration.
3. Firmware testing should occur on both the SIL \(software providing simulation of hardware responses\) and HIL \(integration\) levels. Firmware integration testing is critical to ensure mission success, and should be documented _both_ by virtue of having test software written to automate testing _and_ by filling out test results for major developmental milestones and any tests run for internal design review requirements.
4. Testing should note what version of software is running \(either a release number or a GitHub commit hash\) as well as what revision of hardware was used \(if a HIL test\).
5. Any miscellaneous testing is also very important to document. This includes the radio board with launch rail tests and other such integration tests

### Payload

To be determined once payload\(s\) are selected.

