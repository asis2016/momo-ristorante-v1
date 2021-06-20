def quick_stat_helper_template(title, total, fa_icon):
    html = f"""<div class="col-md-6 col-xl-3 mb-4 quick-stat">
    <div class="card shadow border-start-success py-2">
    <div class="card-body">
    <div class="row align-items-center no-gutters">
    <div class="col me-2">
    <div class="text-uppercase text-success fw-bold text-xs mb-1">
    <span>{title}</span>
    </div>
    <div class="text-dark fw-bold h5 mb-0">
    <span>{total}</span>
    </div>
    </div>
    <div class="col-auto">
    <i class="{fa_icon} fa-2x text-gray-300"></i>
    </div>
    </div>
    </div>
    </div>
    </div>
    """
    return html
