Feature: CureSkin search results

  Scenario: Search results show the right result
    Given Open main page
    When Click Search
    When Search for SPF
    Then Verify the results have SPF