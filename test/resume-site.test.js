import test from 'node:test';
import assert from 'node:assert/strict';
import { profile } from '../resume-site/data.js';

test('resume portfolio contains the public profile essentials', () => {
  assert.equal(profile.name, '홍재선');
  assert.ok(profile.summary.length > 30);
  assert.ok(profile.careers.length >= 3);
  assert.ok(profile.projects.length >= 3);
  assert.ok(profile.skills.includes('Project Management'));
  assert.ok(profile.longSummary.length > profile.summary.length);
  assert.equal(profile.principles.length, 3);
  assert.ok(profile.focusAreas.length >= 4);
});
