@cucumber @candidate @jenkins
Feature: Born 40 Years Ago filter flow
  As a QA team
  I want to validate advanced date filtering on name search results
  So we can run it later as a tagged Cucumber suite in Jenkins

  @born_40_years_ago @smoke @ui
  Scenario: Filter results by birth date exactly 40 years ago
    Given I am on the IMDb home page
    When I open the main menu
    And I navigate to Born Today
    And I remove default birthday chip if present
    And I expand the Birth Date section if needed
    And I set From and To birth dates to 40 years ago
    And I open the first link in the first result description when available
    Then I capture a screenshot for the scenario
