import { validateRegistration } from './src/validation.js';

const form = document.querySelector('#registration-form');
const successMessage = document.querySelector('#success-message');
const fieldNames = ['name', 'email', 'session'];

function showErrors(errors) {
  fieldNames.forEach((fieldName) => {
    const group = document.querySelector(`#${fieldName}`).closest('.field-group');
    const error = document.querySelector(`#${fieldName}-error`);
    const message = errors[fieldName] ?? '';
    group.classList.toggle('has-error', Boolean(message));
    error.textContent = message;
  });
}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  successMessage.textContent = '';

  const formData = new FormData(form);
  const result = validateRegistration({
    name: formData.get('name'),
    email: formData.get('email'),
    session: formData.get('session')
  });

  showErrors(result.errors);
  if (!result.valid) return;

  successMessage.textContent = '신청 정보가 확인되었습니다. 저장 기능은 Supabase 연결 후 활성화됩니다.';
});

form.addEventListener('input', () => {
  successMessage.textContent = '';
});
