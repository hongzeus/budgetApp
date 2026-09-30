import test from 'node:test';
import assert from 'node:assert/strict';
import { validateRegistration } from '../src/validation.js';

test('validates a complete registration with a valid email', () => {
  assert.deepEqual(validateRegistration({
    name: '홍길동',
    email: 'hongzeus@gmail.com',
    session: '2회차 · 오후 2:00'
  }), { valid: true, errors: {} });
});

test('rejects an invalid email and reports the screenshot error message', () => {
  const result = validateRegistration({
    name: '홍길동',
    email: 'hongzeus@gmail',
    session: '2회차 · 오후 2:00'
  });

  assert.equal(result.valid, false);
  assert.equal(result.errors.email, '올바른 이메일을 입력해 주세요.');
});

test('requires the name and selected session', () => {
  const result = validateRegistration({ name: '', email: 'person@example.com', session: '' });

  assert.deepEqual(result.errors, {
    name: '이름을 입력해 주세요.',
    session: '참가 회차를 선택해 주세요.'
  });
});
