function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('mainContent');
    const toggleIcon = document.getElementById('toggleIcon');
    
    sidebar.classList.toggle('collapsed');
    mainContent.classList.toggle('expanded');
    
    if (sidebar.classList.contains('collapsed')) {
        toggleIcon.className = 'fas fa-chevron-right';
    } else {
        toggleIcon.className = 'fas fa-chevron-left';
    }
}

function toggleSubmenu(event) {
    event.preventDefault();
    const submenu = event.target.closest('li').querySelector('.submenu');
    const arrow = event.target.closest('a').querySelector('.submenu-arrow');
    
    submenu.classList.toggle('show');
    arrow.classList.toggle('rotated');
}

        // Mobile sidebar toggle
        function toggleMobileSidebar() {
            const sidebar = document.getElementById('sidebar');
            sidebar.classList.toggle('show');
        }

        // Active menu item handling
        document.querySelectorAll('.nav-menu a').forEach(link => {
            link.addEventListener('click', function(e) {
                // Ne pas empêcher la navigation pour les liens avec href
                if (this.getAttribute('href') !== '#') {
                    return; // Laisser le navigateur suivre le lien
                }
                
                e.preventDefault(); // Empêcher seulement pour les liens #
                
                // Remove active class from all links
                document.querySelectorAll('.nav-menu a').forEach(l => l.classList.remove('active'));
                
                // Add active class to clicked link
                this.classList.add('active');
            });
        });

        // Close sidebar on mobile when clicking outside
        document.addEventListener('click', function(e) {
            const sidebar = document.getElementById('sidebar');
            const mobileToggle = document.querySelector('.mobile-toggle');
            
            if (window.innerWidth <= 768 && 
                !sidebar.contains(e.target) && 
                !mobileToggle.contains(e.target)) {
                sidebar.classList.remove('show');
            }
        });

        // Handle window resize
        window.addEventListener('resize', function() {
            const sidebar = document.getElementById('sidebar');
            if (window.innerWidth > 768) {
                sidebar.classList.remove('show');
            }
        });

        function toggleSubmenu(event) {
            event.preventDefault();
            const submenu = event.currentTarget.nextElementSibling;
            submenu.classList.toggle('active');
        }
function openAddProductionModal() {
    document.getElementById("addProductionModal").style.display = "block";
}

function closeAddProductionModal() {
    document.getElementById("addProductionModal").style.display = "none";
}

window.onclick = function(event) {
    const modal = document.getElementById("addProductionModal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

function openDemoModal() {
    document.getElementById("demoModal").style.display = "block";
}

function closeDemoModal() {
    document.getElementById("demoModal").style.display = "none";
}

// Close modal when clicking the X
document.addEventListener('DOMContentLoaded', function() {
    const closeBtn = document.querySelector('.demo-close');
    if (closeBtn) {
        closeBtn.onclick = function() {
            closeDemoModal();
        }
    }
    
    // Close modal when clicking outside
    window.onclick = function(event) {
        const modal = document.getElementById("demoModal");
        if (event.target == modal) {
            closeDemoModal();
        }
    }
});

function openEditModal(id, nom, prenom) {
    // Change modal title and button for edit mode
    document.getElementById("ajoutEmployeModalLabel").textContent = "Modifier l'employé";
    document.getElementById("submitBtn").textContent = "Modifier";
    document.getElementById("submitBtn").className = "btn btn-primary";
    
    // Fill the form with employee data
    document.getElementById("nom").value = nom;
    document.getElementById("prenom").value = prenom;
    
    // Set form action for edit
    document.getElementById("employeeForm").action = `/modifier_employe/${id}/`;
    
    // Show the modal
    const modal = new bootstrap.Modal(document.getElementById('ajoutEmployeModal'));
    modal.show();
}

function openAddModal() {
    // Reset modal for add mode
    document.getElementById("ajoutEmployeModalLabel").textContent = "Ajouter un employé";
    document.getElementById("submitBtn").textContent = "Ajouter";
    document.getElementById("submitBtn").className = "btn btn-success";
    
    // Clear the form
    document.getElementById("nom").value = "";
    document.getElementById("prenom").value = "";
    
    // Set form action for add
    document.getElementById("employeeForm").action = "{% url 'ajouter_employe' %}";
}

function closeEditEmployeeModal() {
    document.getElementById("editEmployeeModal").style.display = "none";
}

// Add event listener for table rows
document.addEventListener('DOMContentLoaded', function() {
    // Handle table row clicks
    document.querySelectorAll('table tbody tr').forEach(row => {
        row.addEventListener('click', function(e) {
            // Don't trigger if clicking on buttons
            if (e.target.tagName === 'BUTTON' || e.target.tagName === 'A') {
                return;
            }
            
            // Get employee data from the row
            const id = this.getAttribute('data-id');
            const nom = this.getAttribute('data-nom');
            const prenom = this.getAttribute('data-prenom');
            
            if (id && nom && prenom) {
                openEditModal(id, nom, prenom);
            }
        });
    });
});