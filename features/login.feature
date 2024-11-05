Feature: VistaSoft Monitor Login

  Scenario: User can log in to VSM and view the dashboard
    Given I open the VSM login page
    When I enter valid credentials
    Then I should be redirected to the VSM dashboard
    And the URL should be "https://vsmonitor.com/dashboard"

  Scenario: User can view account information
    Given I am logged into VSM
    When I navigate to "My user account"
    Then I should see my name and email
    And the URL should be "https://vsmonitor.com/user/profile"