@cucumber @candidate @jenkins
Feature: Born Yesterday filter flow
  As a QA team
  I want to validate the Born Today page filtering to yesterday
  So we can run it later as a tagged Cucumber suite in Jenkins

  @born_yesterday @smoke @ui
  Scenario: Filter Born Today to yesterday and open third person
    Given I am on the IMDb home page
    When I open the main menu
    And I navigate to Born Today
    Then the Born Today date in URL should match today
    When I expand the Birthday filter if needed
    And I set Birthday filter to yesterday
    And I open the third person in results
    Then I capture a screenshot for the scenario
