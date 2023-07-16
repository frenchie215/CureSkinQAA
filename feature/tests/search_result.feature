Feature: CureSkin search results

  Scenario: Search results show the right result
    Given Open main page
    When Click search button
    When Input text SPF
    Then Verify the text SPF is shown