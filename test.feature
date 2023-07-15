#Feature: Product names and images
#
#Scenario: User can see product names and images
#    Given Open Amazon page
#    When Input text coffee
#    When Click on search button
#    Then Verify that every product has a name and an image

Feature: Test Scenarios for Sign In

  Scenario: User sees sign in page
    Given Open Amazon page
    When Click Orders
    Then Verify Sign In page opens


Scenario: Sign in page can be opened from SignIn popup
  Given Open Amazon page
  When Click on button from Signin popup
  Then Verify Sign In page opens


Scenario: Sign in popup is visible for a few seconds
  Given Open Amazon page
  Then Verify sign in popup shown
  When Wait for 8 sec
  Then Verify Sign In popup disappears
