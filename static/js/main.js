const searchForm = document.querySelector("#searchForm");
const pageLinks = document.querySelectorAll(".page-link");

if (searchForm) {
    for (const link of pageLinks) {
        link.addEventListener("click", function(e) {
            e.preventDefault();

            let page = this.dataset.page;

            searchForm.innerHTML += `<input type="hidden" name="page" value="${page}" />`;

            searchForm.submit();
        });
    }
}

const tags = document.querySelectorAll(".project-tag");


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

for (const tag of tags) {
    tag.addEventListener("click", async(e) => {
        const tagId = e.target.dataset.tag;
        const projectId = e.target.dataset.project;

        const res = await fetch("http://127.0.0.1:8000/api/remove-tag/", {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({ project: projectId, tag: tagId }),
        });

        const data = await res.json();

        if (data) {
            e.target.remove();
        }
    });
}