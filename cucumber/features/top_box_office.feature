@cucumber @candidate @jenkins
Feature: Top Box Office rating flow
  As a QA team
  I want to validate the Top Box Office rating interaction
  So we can run it later as a tagged Cucumber suite in Jenkins

  @top_box_office @smoke @ui
  Scenario: Rate the second Top Box Office title with five stars
    Given I am on the IMDb home page
    When I open the main menu
    And I navigate to Top Box Office
    Then I should be on the Top Box Office page
    When I open the second title from Top Box Office
    And I open the user rating modal
    And I rate the title with five stars and confirm
    Then I should either be asked to sign in or see the rating modal closed
