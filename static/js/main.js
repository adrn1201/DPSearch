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

for (const tag of tags) {
    tag.addEventListener("click", async(e) => {
        const tagId = e.target.dataset.tag;
        const projectId = e.target.dataset.project;

        const res = await fetch("http://127.0.0.1:8000/api/remove-tag/", {
            method: "DELETE",
            headers: {
                "Content-type": "application/json",
            },
            body: JSON.stringify({ project: projectId, tag: tagId }),
        });

        const data = await res.json();

        if (data) {
            e.target.remove();
        }
    });
}