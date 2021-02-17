
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
    ]
  },
  {
    path: '/about',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/About.vue') }
    ]
  },
  {
    path: '/projects',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Projects.vue') },
      { path: ':slug',  params: 'slug', component: () => import('pages/ProjectDetail.vue') }
    ]
  },
  {
    path: '/blog',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Blog.vue') },
      { path: ':slug', params: 'slug', component: () => import('pages/Blog.vue') },
      { path: 'post/:slug',  params: 'slug', component: () => import('pages/PostDetail.vue') }
    ]
  },
  {
    path: '/forum',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Forum.vue') },
      { path: ':slug', params: 'slug', component: () => import('pages/ForumThemeDetail.vue') },
    ]
  },
  {
    path: '/activities',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Activities') },
    ]
  },
  {
    path: '/rules',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/SiteRules.vue') },
    ]
  },
  {
    path: '/questions',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Questions.vue') },
    ]
  },
  {
    path: '/contacts',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Contacts') },
    ]
  },
  {
    path: '/partner_forms',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/PartnerForms.vue') },
      { path: ':slug', params: 'slug', component: () => import('pages/PartnerFormDetail') },
    ]
  },
  {
    path: '/profile',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/ProfileDetail') },
      { path: ':id', params: 'id', component: () => import('pages/ProfileDetail') },
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
