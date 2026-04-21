@cucumber @candidate @jenkins
Feature: Breaking Bad photos filter flow
  As a QA team
  I want to validate photo filtering on Breaking Bad
  So we can run it later as a tagged Cucumber suite in Jenkins

  @breaking_bad_photos @smoke @ui
  Scenario: Filter Breaking Bad photos by Danny Trejo and open image
    Given I am on the IMDb home page
    When I open the main menu
    And I navigate to Top 250 TV Shows
    Then I should be on the Top TV page
    When I open the Breaking Bad title page
    And I open the Photos section
    And I open the gallery
    And I open the photo filter prompt
    And I apply person filter "Danny Trejo"
    And I close the photo filter prompt
    Then I should see person filter "Danny Trejo" applied
    When I open the second filtered image
    Then I should be on a media viewer page
