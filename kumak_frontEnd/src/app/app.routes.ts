import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { HeaderComponent } from './header/header.component';
import { AboutComponent } from './about/about.component';
import { CategoriesComponent } from './categories/categories.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { TablewareComponent } from './tableware/tableware.component';
import { ContactsComponent } from './contacts/contacts.component';
import { FurnitureComponent } from './furniture/furniture.component';
import { TextilesComponent } from './textiles/textiles.component';
import { OCPComponent } from './OrganicCleaningProduct/OCP.component';
import { PaintComponent } from './paint/paint.component';
import { DecorComponent } from './decor/decor.component';

export const routes: Routes = [
    {path: '', component: HeaderComponent},
    {path: 'login', component: LoginComponent},
    {path: 'about', component: AboutComponent},
    {path: 'categories', component: CategoriesComponent},
    {path: 'categories/:id/Tableware', component: TablewareComponent},
    {path: 'categories/:id/Textiles', component: TextilesComponent},
    {path: 'categories/:id/Keys', component: TextilesComponent},
    {path: 'categories/:id/OrganicCleaningProduct', component: OCPComponent},
    {path: 'categories/:id/Paint', component: PaintComponent},
    {path: 'categories/:id/Decor', component: DecorComponent},
    {path: 'categories/:id/Furniture', component: FurnitureComponent},
    {path: 'contacts', component: ContactsComponent},
    {path: '**', component: NotFoundComponent},

];
