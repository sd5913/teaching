# GitHub deployment screenshots

Retrieved 18 November 2026 for the 19 November lesson. These are real UI
captures, with no credential values or student data. GitHub UI is reproduced
to explain the course repository workflow; no UI is generated or redrawn.

## Course repository captures

Public, signed-out browser, 1720 x 1040 viewport. Template source pin:
`69cbed7363412daa4a7e8c2c8fc4ed02a3f1afa5`.

| Asset | Source |
| --- | --- |
| github-template.png | https://github.com/sd5913/github-oauth-d1-template |
| github-deploy-trigger.png | Crop of actual source view, lines 1-5: https://github.com/sd5913/github-oauth-d1-template/blob/69cbed7363412daa4a7e8c2c8fc4ed02a3f1afa5/.github/workflows/deploy.yml |
| github-deploy-runs.png | https://github.com/sd5913/github-oauth-d1-template/actions/workflows/deploy.yml |
| github-actions-checks.png | https://github.com/sd5913/github-oauth-d1-template/actions/runs/43684401618 |

All projection images are unaltered rectangular crops of the original
viewport capture, enlarged in the native slide layout:

| Projection image | Original viewport | Crop (left,top)-(right,bottom) |
| --- | --- | --- |
| github-template-overview.png | github-template.png | (250,178)-(1120,560) |
| github-deploy-trigger.png | deploy.yml source | (375,342)-(835,450) |
| github-workflow-selection.png | github-deploy-runs.png | (0,80)-(700,225) |
| github-workflow-run.png | github-deploy-runs.png | (410,258)-(1070,320) |
| github-check-summary.png | github-actions-checks.png | (375,285)-(925,355) |
| github-check-job.png | github-actions-checks.png | (380,498)-(644,549) |

The filename/pin and source are in the relevant slide caption or notes.
Splitting metadata and job regions lets students read them without the large
blank lower portion of the browser viewport.

Checks passed for that public template revision. Its deployment configuration
is absent: the configuration job passes and the deploy job skips. This is
not evidence of a live Cloudflare deployment, working OAuth or two-account
acceptance. No workflow button was pressed during authoring.

## GitHub Docs control images

Attribution: GitHub, Inc. and GitHub Docs contributors, GitHub Docs,
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
Licence: https://github.com/github/docs/blob/main/LICENSE . Images copied
unchanged, scaled to fit the slide. Retrieved 18 November 2026.

| Asset | Original image | Documentation |
| --- | --- | --- |
| github-use-template.png | https://raw.githubusercontent.com/github/docs/main/assets/images/help/repository/use-this-template-button.png | https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template |
| github-secrets.png | https://docs.github.com/assets/images/help/repository/actions-secrets-tab.png | https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets |
| github-run-workflow.png | https://docs.github.com/assets/images/help/actions/actions-workflow-dispatch.png | https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow |

These illustrate the signed-in controls missing from the public signed-out
capture. The manual-run screenshot says **Browser Tests**, an illustrative
documentation workflow. In the course exercise select **Deploy to Cloudflare**.
The caption and notes explicitly identify this distinction.
