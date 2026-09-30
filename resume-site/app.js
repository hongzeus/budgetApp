import { profile } from './data.js';

const byId = (id) => document.getElementById(id);

document.querySelectorAll('[data-profile]').forEach((element) => {
  const key = element.dataset.profile;
  element.textContent = profile[key];
});

byId('stats').innerHTML = profile.stats.map((stat) => `<div class="stat"><strong>${stat.value}</strong><span>${stat.label}</span></div>`).join('');

byId('careers').innerHTML = profile.careers.map((career) => `
  <article class="timeline-item"><time>${career.period}</time><div><h3>${career.company}</h3><p>${career.role}</p><small>${career.detail}</small></div></article>
`).join('');

byId('projects').innerHTML = profile.projects.map((project, index) => `
  <article class="project-card ${project.color}"><div class="project-top"><span>${project.tag}</span><span>0${index + 1}</span></div><div><h3>${project.title}</h3><p>${project.description}</p><small>${project.role}</small></div><div class="project-arrow">↗</div></article>
`).join('');

byId('focus-areas').innerHTML = profile.focusAreas.map((area) => `<span>${area}</span>`).join('');
byId('principles').innerHTML = profile.principles.map((principle) => `<article class="principle"><span class="principle-number">${principle.number}</span><h3>${principle.title}</h3><p>${principle.text}</p></article>`).join('');

byId('skills').innerHTML = profile.skills.map((skill) => `<span>${skill}</span>`).join('');

byId('certificates').innerHTML = profile.certificates.map((certificate) => `<div class="credential-row"><strong>${certificate.name}</strong><span>${certificate.date}</span></div>`).join('');
byId('learning').innerHTML = profile.learning.map((item) => `<div class="learning-row"><span>↗</span><strong>${item}</strong></div>`).join('');

document.querySelector('[data-contact="email"]').href = `mailto:${profile.email}`;
document.querySelector('[data-contact="phone"]').href = `tel:${profile.phone.replaceAll('-', '')}`;
