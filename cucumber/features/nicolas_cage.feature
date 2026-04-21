@cucumber @candidate @jenkins
Feature: Nicolas Cage upcoming completed navigation
  As a QA team
  I want to validate the Nicolas Cage upcoming credits flow
  So we can run it later as a tagged Cucumber suite in Jenkins

  @nicolas_cage @smoke @ui
  Scenario: Open first upcoming title marked as Completed
    Given I am on the IMDb home page
    When I search for "Nicolas Cage"
    And I open the Nicolas Cage profile
    And I scroll to the Credits section
    And I expand the Upcoming section if needed
    And I open the first upcoming title with status "Completed"
    Then I should be navigated to a title page
