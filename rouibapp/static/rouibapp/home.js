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

// =========================
//  Active Link Management
// =========================
document.querySelectorAll('.nav-menu a').forEach(link => {
    link.addEventListener('click', function (e) {
        // Laisser passer tous les liens qui ne sont pas juste "#"
        if (this.getAttribute('href') && this.getAttribute('href') !== '#') {
            return;
        }
        e.preventDefault();

        document.querySelectorAll('.nav-menu a').forEach(l => l.classList.remove('active'));
        this.classList.add('active');
    });
});

// =========================
//  Close Sidebar on Mobile
// =========================
document.addEventListener('click', function (e) {
    const sidebar = document.getElementById('sidebar');
    const mobileToggle = document.querySelector('.mobile-toggle');

    if (window.innerWidth <= 768 &&
        !sidebar.contains(e.target) &&
        !mobileToggle?.contains(e.target)) {
        sidebar.classList.remove('show');
    }
});

// =========================
//  Handle Resize
// =========================
window.addEventListener('resize', function () {
    const sidebar = document.getElementById('sidebar');
    if (window.innerWidth > 768) {
        sidebar.classList.remove('show');
    }
});

// =========================
//  Modal Functions
// =========================
function openAddProductionModal() {
    document.getElementById("addProductionModal").style.display = "block";
}

function closeAddProductionModal() {
    document.getElementById("addProductionModal").style.display = "none";
}

function openDemoModal() {
    document.getElementById("demoModal").style.display = "block";
}

function closeDemoModal() {
    document.getElementById("demoModal").style.display = "none";
}

document.addEventListener('DOMContentLoaded', function () {
    const closeBtn = document.querySelector('.demo-close');
    if (closeBtn) closeBtn.onclick = closeDemoModal;

    window.onclick = function (event) {
        const modals = ["demoModal", "addProductionModal"];
        modals.forEach(id => {
            const modal = document.getElementById(id);
            if (event.target === modal) modal.style.display = "none";
        });
    }
});

// =========================
//  Production Table Actions
// =========================
let ligneSelectionneeProduction = null;

function selectionnerLigneProduction(ligne) {
    if (ligneSelectionneeProduction) {
        ligneSelectionneeProduction.classList.remove('selected');
    }
    ligneSelectionneeProduction = ligne;
    ligne.classList.add('selected');

    document.getElementById('modifierBtn').style.display = 'inline-block';
    document.getElementById('supprimerBtn').style.display = 'inline-block';
}

function modifierProduction() {
    if (!ligneSelectionneeProduction) return;

    const productionId = ligneSelectionneeProduction.dataset.productionId;
    const cells = ligneSelectionneeProduction.getElementsByTagName('td');

    document.getElementById('date_mod').value = cells[0].textContent;
    document.getElementById('ligne_mod').value = cells[1].dataset.ligneId;
    document.getElementById('quart_mod').value = cells[2].dataset.quartId;
    document.getElementById('format_mod').value = cells[3].dataset.formatId;
    document.getElementById('cadence_mod').value = cells[4].textContent;
    document.getElementById('temps_brut_mod').value = cells[5].textContent;
    document.getElementById('temps_programme_mod').value = cells[6].textContent;
    document.getElementById('temps_non_programme_mod').value = cells[7].textContent;
    document.getElementById('theorique_mod').value = cells[8].textContent;
    document.getElementById('realise_mod').value = cells[9].textContent;
    document.getElementById('trs_mod').value = cells[10].textContent;
    document.getElementById('c_mod').value = cells[11].textContent;
    document.getElementById('perte_mod').value = cells[12].textContent;
    document.getElementById('nep_complet_mp_theorique_mod').value = cells[13].textContent;
    document.getElementById('nep_complet_mp_reel_mod').value = cells[14].textContent;
    document.getElementById('nep_complet_ecart_mod').value = cells[15].textContent;

    document.getElementById('formModifierProduction').action = `/carton/edit/${productionId}/`;

    const modalElement = document.getElementById('modifierProductionModal');
    if (modalElement) {
        const modal = new bootstrap.Modal(modalElement);
        modal.show();
    }
}

function supprimerProduction() {
    if (!ligneSelectionneeProduction) return;

    const productionId = ligneSelectionneeProduction.dataset.productionId;
    if (confirm('Êtes-vous sûr de vouloir supprimer cette production ?')) {
        window.location.href = `/carton/delete/${productionId}/`;
    }
}