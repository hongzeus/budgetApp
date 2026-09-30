const EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export function validateRegistration({ name = '', email = '', session = '' }) {
  const errors = {};

  if (!name.trim()) errors.name = '이름을 입력해 주세요.';
  if (!EMAIL_PATTERN.test(email.trim())) errors.email = '올바른 이메일을 입력해 주세요.';
  if (!session.trim()) errors.session = '참가 회차를 선택해 주세요.';

  return { valid: Object.keys(errors).length === 0, errors };
}
