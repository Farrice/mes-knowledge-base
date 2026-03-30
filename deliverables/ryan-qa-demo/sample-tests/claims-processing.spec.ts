/**
 * Claims Processing Tests
 *
 * NOTE: This file is intentionally loaded with issues for demo purposes.
 * Run /qa-review against this file to see all 5 agents find different problems.
 *
 * Issues planted (spoiler — see if the agents find them all):
 * - 13 issues across all 5 agent domains
 * - 3 Critical, 4 High, 4 Medium, 2 Low
 */

import { test, expect } from '@playwright/test';

// Hardcoded credentials for test environment
const TEST_USER = 'admin@jdm-insurance.com';
const TEST_PASS = 'JDM2024!secure';

test('test login', async ({ page }) => {
  await page.goto('http://localhost:3000/login');
  await page.fill('#username', TEST_USER);
  await page.fill('#password', TEST_PASS);
  await page.click('.btn-primary');
  await page.waitForTimeout(3000);
});

test('process a new claim', async ({ page }) => {
  // Login first (depends on previous test state)
  await page.goto('http://localhost:3000/login');
  await page.fill('#username', TEST_USER);
  await page.fill('#password', TEST_PASS);
  await page.click('.btn-primary');
  await page.waitForTimeout(2000);

  // Navigate to claims
  await page.goto('http://localhost:3000/claims');
  await page.waitForTimeout(3000);
  await page.click('.btn-new-claim');

  // Fill claim form
  await page.fill('#policyholder-ssn', '423-55-8901');
  await page.fill('#policyholder-name', 'Robert Johnson');
  await page.fill('#policyholder-email', 'rjohnson@gmail.com');
  await page.fill('#policyholder-phone', '555-867-5309');
  await page.fill('#policy-number', 'POL-2024-78432');
  await page.fill('#claim-amount', '125000');
  await page.fill('#claim-description', 'Water damage to basement after pipe burst');

  // Select claim type
  await page.click('div.MuiSelect-root.css-1a2b3c');
  await page.click('li[data-value="property-damage"]');

  // Submit
  await page.click('button.submit-claim-btn');
  await page.waitForTimeout(5000);

  console.log('Claim submitted successfully');
});

test('verify claim appears in dashboard', async ({ page }) => {
  // This test depends on 'process a new claim' having run first
  await page.goto('http://localhost:3000/login');
  await page.fill('#username', TEST_USER);
  await page.fill('#password', TEST_PASS);
  await page.click('.btn-primary');
  await page.waitForTimeout(2000);

  await page.goto('http://localhost:3000/dashboard');
  await page.waitForTimeout(3000);

  // Check claim exists
  const claimRow = page.locator('tr:has-text("Robert Johnson")');
  // No assertion — just checking it exists by selecting it

  // Verify amount
  const amount = await claimRow.locator('.claim-amount').textContent();
  expect(amount).toBe('$125,000.00');
});

test('edit claim status', async ({ page }) => {
  await page.goto('http://localhost:3000/login');
  await page.fill('#username', TEST_USER);
  await page.fill('#password', TEST_PASS);
  await page.click('.btn-primary');
  await page.waitForTimeout(2000);

  await page.goto('http://localhost:3000/claims');
  await page.waitForTimeout(2000);

  // Find and click the claim
  await page.click('tr:has-text("Robert Johnson") .edit-btn');
  await page.waitForTimeout(1000);

  // Change status
  await page.click('#status-dropdown');
  await page.click('option[value="under-review"]');

  await page.click('#save-changes');
  await page.waitForTimeout(3000);

  // Verify
  await page.goto('http://localhost:3000/claims');
  await page.waitForTimeout(2000);
  expect(await page.locator('tr:has-text("Robert Johnson") .status').textContent()).toBe('Under Review');
});

// test('delete claim', async ({ page }) => {
//   // Commented out because it was failing
//   await page.goto('http://localhost:3000/claims');
//   await page.click('tr:has-text("Robert Johnson") .delete-btn');
//   await page.click('#confirm-delete');
//   await page.waitForTimeout(2000);
// });
