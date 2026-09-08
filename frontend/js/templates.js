/* =========================================================
   Email Templates page
   ========================================================= */

Api.requireAuth();

const form = document.getElementById("templateForm");
const formTitle = document.getElementById("formTitle");
const nameInput = document.getElementById("templateName");
const categoryInput = document.getElementById("templateCategory");
const contentInput = document.getElementById("templateContent");
const saveButton = document.getElementById("saveTemplateBtn");
const cancelButton = document.getElementById("cancelEditBtn");
const filterInput = document.getElementById("templateFilter");
const container = document.getElementById("templatesContainer");

let templates = [];
let editingId = null;

/* ---------------------------------------------------------
   Load templates
   --------------------------------------------------------- */

async function loadTemplates() {
    try {
        container.innerHTML = "<p>Loading templates...</p>";

        templates = await Api.getTemplates();

        renderTemplates();

    } catch (error) {
        container.innerHTML =
            `<p class="template-empty">${escapeHtml(error.message)}</p>`;
    }
}

/* ---------------------------------------------------------
   Render templates
   --------------------------------------------------------- */

function renderTemplates() {

    const filter = filterInput.value;

    let filteredTemplates = templates;

    if (filter !== "All") {
        filteredTemplates = templates.filter(
            template => template.category === filter
        );
    }

    if (filteredTemplates.length === 0) {

        container.innerHTML = `
            <div class="template-empty">
                <p>No templates found.</p>
            </div>
        `;

        return;
    }

    container.innerHTML = filteredTemplates.map(template => {

        return `
            <article class="template-card">

                <div class="template-header">

                    <h3 class="template-name">
                        ${escapeHtml(template.name)}
                    </h3>

                    <span class="template-category">
                        ${escapeHtml(template.category)}
                    </span>

                </div>

                <div class="template-content">
                    ${escapeHtml(template.content)}
                </div>

                <div class="template-actions">

                    <button
                        type="button"
                        class="btn btn-secondary"
                        onclick="copyTemplate(${template.id})">
                        Copy
                    </button>

                    <button
                        type="button"
                        class="btn btn-secondary"
                        onclick="editTemplate(${template.id})">
                        Edit
                    </button>

                    <button
                        type="button"
                        class="btn btn-danger"
                        onclick="deleteTemplate(${template.id})">
                        Delete
                    </button>

                </div>

            </article>
        `;

    }).join("");
}

/* ---------------------------------------------------------
   Create / Update template
   --------------------------------------------------------- */

form.addEventListener("submit", async function (event) {

    event.preventDefault();

    const data = {
        name: nameInput.value.trim(),
        category: categoryInput.value,
        content: contentInput.value.trim()
    };

    try {

        saveButton.disabled = true;

        if (editingId === null) {

            await Api.createTemplate(data);

            if (typeof showToast === "function") {
                showToast("Template created successfully.");
            }

        } else {

            await Api.updateTemplate(editingId, data);

            if (typeof showToast === "function") {
                showToast("Template updated successfully.");
            }

        }

        resetForm();
        await loadTemplates();

    } catch (error) {

        if (typeof showToast === "function") {
            showToast(error.message, "error");
        } else {
            alert(error.message);
        }

    } finally {
        saveButton.disabled = false;
    }
});

/* ---------------------------------------------------------
   Edit template
   --------------------------------------------------------- */

function editTemplate(id) {

    const template = templates.find(
        item => item.id === id
    );

    if (!template) {
        return;
    }

    editingId = id;

    nameInput.value = template.name;
    categoryInput.value = template.category;
    contentInput.value = template.content;

    formTitle.textContent = "Edit Template";
    saveButton.textContent = "Update Template";
    cancelButton.style.display = "inline-flex";

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}

/* ---------------------------------------------------------
   Cancel edit
   --------------------------------------------------------- */

cancelButton.addEventListener("click", function () {
    resetForm();
});

/* ---------------------------------------------------------
   Reset form
   --------------------------------------------------------- */

function resetForm() {

    editingId = null;

    form.reset();

    formTitle.textContent = "Create New Template";
    saveButton.textContent = "Save Template";
    cancelButton.style.display = "none";
}

/* ---------------------------------------------------------
   Delete template
   --------------------------------------------------------- */

async function deleteTemplate(id) {

    const template = templates.find(
        item => item.id === id
    );

    if (!template) {
        return;
    }

    const confirmed = confirm(
        `Delete "${template.name}"?`
    );

    if (!confirmed) {
        return;
    }

    try {

        await Api.deleteTemplate(id);

        if (typeof showToast === "function") {
            showToast("Template deleted successfully.");
        }

        await loadTemplates();

    } catch (error) {

        if (typeof showToast === "function") {
            showToast(error.message, "error");
        } else {
            alert(error.message);
        }
    }
}

/* ---------------------------------------------------------
   Copy template
   --------------------------------------------------------- */

async function copyTemplate(id) {

    const template = templates.find(
        item => item.id === id
    );

    if (!template) {
        return;
    }

    try {

        await navigator.clipboard.writeText(
            template.content
        );

        if (typeof showToast === "function") {
            showToast("Template copied to clipboard.");
        }

    } catch (error) {

        alert("Unable to copy template.");
    }
}

/* ---------------------------------------------------------
   Filter
   --------------------------------------------------------- */

filterInput.addEventListener("change", function () {
    renderTemplates();
});

/* ---------------------------------------------------------
   HTML escaping
   --------------------------------------------------------- */

function escapeHtml(value) {

    const div = document.createElement("div");

    div.textContent = value ?? "";

    return div.innerHTML;
}

/* ---------------------------------------------------------
   Initial load
   --------------------------------------------------------- */

loadTemplates();
