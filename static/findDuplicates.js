document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    const template = JSON.parse(document.getElementsByTagName('main')[0].dataset.template),
          baseUrl = document.querySelector('link[rel=index]').href,
          lemmaInput = document.querySelector('input[name=form_representation]'),
          lexemeIdInput = document.querySelector('input[name=lexeme_id]');

    function removeElementById(id) {
        const element = document.getElementById(id);
        if (element) {
            element.remove();
        }
    }

    function checkDuplicates(e) {
        removeElementById('duplicates-warning');
        removeElementById('no-duplicate');

        const lemma = e.target.value.split('/', 1)[0];
        if (lemma === '') {
            return;
        }

        if (lexemeIdInput && lexemeIdInput.value) {
            return;
        }

        const url = `${baseUrl}api/v1/duplicates/${'test' in template ? 'test' : 'www'}/${template.language_code}/${encodeURIComponent(lemma)}?template_name=${template['@template_name']}`,
              init = {
                  headers: {
                      Accept: 'text/html'
                  }
              };
        fetch(url, init).then(response => response.text()).then(duplicatesWarningHtml => {
            if (duplicatesWarningHtml === '') {
                return;
            }

            const url = `${baseUrl}api/v1/no_duplicate/${template.language_code}`;
            return fetch(url, init).then(response => response.text()).then(noDuplicateHtml => {
                const duplicatesWarning = document.createElement('div');
                document.querySelector('form').insertAdjacentElement('afterbegin', duplicatesWarning);
                duplicatesWarning.outerHTML = duplicatesWarningHtml;

                const noDuplicate = document.createElement('label');
                document.getElementById('submit').insertAdjacentElement('beforebegin', noDuplicate);
                noDuplicate.outerHTML = noDuplicateHtml;
            });
        }).catch(console.error);
    }

    const checkDebounced = _.debounce(checkDuplicates, 500);
    lemmaInput.addEventListener('input', checkDebounced);
    lemmaInput.addEventListener('change', checkDebounced.flush);

    checkDuplicates({ target: lemmaInput });
});
